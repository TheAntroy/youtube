from django import forms

from books.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

        widgets = {
            "year": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields["title"].label = "Book Title"
        self.fields["year"].label = "Year Published"
        self.fields["images"].label = "Image URL"

        for _, field in self.fields.items():
            field.required = True

            field.widget.attrs.update(
                {
                    "class": "block w-full px-4 py-3 mt-2 text-sm text-gray-700 bg-white border border-gray-200 rounded-md focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40",
                }
            )
