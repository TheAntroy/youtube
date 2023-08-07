<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mengirim Email</title>
</head>
<body>
    <form action="sender.php" method="post">
        <textarea name="subjek" id="" cols="30" rows="10" placeholder="subjek"></textarea>
        <input type="email" name="email" placeholder="email">
        <input type="text" name="nama_penerima" placeholder="nama penerima">
        <textarea name="body" id="" cols="30" rows="10" placeholder="body email"></textarea>
        <button type="submit" name="submit">Kirim</button>
    </form>

</body>
</html>