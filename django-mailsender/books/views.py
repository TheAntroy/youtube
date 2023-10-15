from django.shortcuts import render, redirect
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings

from books.forms import BookForm
from books.models import Books

# Create your views here.


# Fungsi untuk menampilkan daftar buku
def list_books(request):
    title = "Home"
    books = Books.objects.all()

    context = {
        "books": books,
        "title": title,
    }
    return render(request, "books/index.html", context)


# Fungsi untuk menghapus buku
def delete_book(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        # Simpan judul dan contact buku untuk digunakan dalam pesan email
        book_title = book.title
        book_contact = book.contact
        book.delete()

        subject = f"Buku Dihapus: {book_title}"
        message = f"Buku dengan judul '{book_title}' telah dihapus dari online library."

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [book_contact],
            fail_silently=False,
        )

        return redirect("books:list_books")
    except Books.DoesNotExist:
        raise Http404("Book not found")


# Fungsi untuk menampilkan formulir buku
def display_book_form(request):
    book_id = request.GET.get("book_id")
    title = "Add new" if book_id is None else "Update"
    book = None

    if book_id:
        try:
            book = Books.objects.get(id=book_id)
        except Books.DoesNotExist:
            raise Http404("Book not found")

    subject = ""
    message = ""
    new_book_contact = None  # Inisialisasi new_book_contact sebagai None

    if request.method == "POST":
        if book:
            forms = BookForm(request.POST, instance=book)
            if forms.is_valid() and forms.has_changed():
                # Buat pesan untuk perubahan buku
                subject = f"Perbarui Buku: {book.title}"
                message = f"Informasi buku '{book.title}' telah diperbarui."
                forms.save()
        else:
            forms = BookForm(request.POST)
            if forms.is_valid():
                # Buat pesan untuk penambahan buku baru
                new_book_title = (
                    forms.instance.title if forms.instance.title else "Tidak ada judul"
                )
                new_book_contact = forms.instance.contact
                subject = "Tambahkan Buku Baru"
                message = f"Buku baru dengan judul '{new_book_title}' telah ditambahkan ke dalam online library."

                forms.save()

        if subject and message:
            # Kirim email hanya jika subjek dan pesan sudah diisi
            # Menggunakan new_book_contact jika ada, jika tidak, gunakan book.contact
            contact = (
                new_book_contact
                if new_book_contact
                else (book.contact if book else None)
            )
            if contact:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [contact],
                    fail_silently=False,
                )

        return redirect("books:list_books")
    else:
        if book:
            forms = BookForm(instance=book)
        else:
            forms = BookForm()

    context = {
        "forms": forms,
        "title": title,
    }
    return render(request, "books/forms.html", context)
