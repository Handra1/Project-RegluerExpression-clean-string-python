# Project-RegluerExpression-clean-string-python
This project about using regluer expression to clean strings in python (In Indonesia)

String Manipulation: Banyak proses data cleaning melibatkan manipulasi string, karena sebagian data banyak yang tidak terstruktur. Manipulasi string juga dilakukan untuk membuat datasets bersifat konsisten ketika ingin mengkombinasikan data secara bersamaan.
Misalkan terdapat string yang mengandung nilai mata uang. Seperti:
- 17 : integer.
- $17 : integer dengan simbol dollar.
- $17.89 : angka float dengan simbol dollar dan 2 digit setelah angka decimal.

Kita akan mengecek dan melakukan validasi terhadap nilai tersebut, sehingga kita mengetahui jika terdapat error.
Python memiliki method dan library untuk manipulasi string, misalnya ‘re’ library untuk regular expression yang digunakan untuk mencocokan bentuk (pattern) string. Sebelumnya kita sudah belajar tentang module ‘glob’ untuk mencocokan pattern.

- Contoh: 17:
Misalnya kita ingin mencocokan semua angka numerik maka kita dapat menggunakan regex pattern backslash d untuk mendapatkan digit nilai diikuti dengan simbol asterik:
\d* : 123456678901

- Contoh : $17:
Untuk integer yang memiliki simbol dollar yang sebenarnya memiliki arti khusus di regex, maka yang kita lakukan dengan menambahkan backslash simbol dollar:
\$\d* : $12345678901

- Contoh: $17.00:
Pada pencocokan nilai mata uang dengan angka decimal, kita tambahkan dengan diikuti digit yang lebih banyak:
\$\d*\.\d* : $12345678901.42

- Contoh: $17.89:
Untuk penulisan regex angka decimal, selain menggunakan cara pertama kita juga dapat menuliskan dengan curly bracket { } diikuti dengan banyaknya angka decimal yang kita inginkan:
\$\d*.\d{2}  : $12345678901.24

Untuk menggunakan regular expression, cara yang paling efisien adalah mengcompile pattern terlebih dulu, baru kemudian kita cocokan pattern tersebut dengan nilai yang ada. Kita bisa memanfaatkan package pandas untuk melakukan validasi nilai dengan menggunakan method ‘re’.
Jadi disini kita gunakan method pencocokan pattern ke string dengan cara menginput string yang ingin kita cocokan. Hingga akhirnya menghasilkan objek pencocokan. Maka kita mendapatkan nilai true or false boolean.
