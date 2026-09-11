import tkinter as tk
from tkinter import messagebox


# =========================
# ZIG-ZAG CIPHER
# =========================

def encrypt(text, rails):

    if rails <= 1:
        return text

    fence = [""] * rails
    row = 0
    direction = 1

    for char in text:

        fence[row] += char

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row += direction


    return "".join(fence)



def decrypt(cipher, rails):

    if rails <= 1:
        return cipher


    pattern = []

    row = 0
    direction = 1


    for i in range(len(cipher)):

        pattern.append(row)

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row += direction



    rails_data = []

    index = 0


    for r in range(rails):

        jumlah = pattern.count(r)

        rails_data.append(
            list(cipher[index:index+jumlah])
        )

        index += jumlah



    hasil = ""


    for posisi in pattern:

        hasil += rails_data[posisi].pop(0)


    return hasil



# =========================
# BUTTON FUNCTION
# =========================


def enkripsi():

    try:

        pesan = input_pesan.get()

        rail = int(input_rail.get())


        hasil = encrypt(
            pesan,
            rail
        )


        tampilkan_hasil(
            "HASIL ENKRIPSI",
            hasil
        )


    except:

        messagebox.showerror(
            "Error",
            "Jumlah rail harus angka!"
        )



def dekripsi():

    try:

        pesan = input_pesan.get()

        rail = int(input_rail.get())


        hasil = decrypt(
            pesan,
            rail
        )


        tampilkan_hasil(
            "HASIL DEKRIPSI",
            hasil
        )


    except:

        messagebox.showerror(
            "Error",
            "Jumlah rail harus angka!"
        )



def tampilkan_hasil(judul, hasil):

    output.delete(
        "1.0",
        tk.END
    )

    output.insert(
        tk.END,
        judul + "\n\n"
    )

    output.insert(
        tk.END,
        hasil
    )



def reset():

    input_pesan.delete(
        0,
        tk.END
    )

    input_rail.delete(
        0,
        tk.END
    )

    output.delete(
        "1.0",
        tk.END
    )



# =========================
# DESAIN GUI
# =========================

app = tk.Tk()

app.title("🔐 Zig-Zag Cipher")

app.geometry("600x700")

app.resizable(False, False)

app.configure(
    bg="#DDF3FF"
)


# JUDUL

judul = tk.Label(
    app,
    text="🔐 ZIG-ZAG CIPHER",
    font=("Arial", 26, "bold"),
    fg="#1769AA",
    bg="#DDF3FF"
)

judul.pack(pady=15)



sub = tk.Label(
    app,
    text="Classic Cryptography Application",
    font=("Arial", 11),
    bg="#DDF3FF"
)

sub.pack()



# BOX INPUT

frame = tk.Frame(
    app,
    bg="white",
    padx=40,
    pady=20
)

frame.pack(pady=20)



tk.Label(
    frame,
    text="Masukkan Pesan",
    font=("Arial", 12, "bold"),
    bg="white"
).pack()


input_pesan = tk.Entry(
    frame,
    width=40,
    font=("Arial", 12)
)

input_pesan.pack(
    pady=10
)



tk.Label(
    frame,
    text="Jumlah Rail",
    font=("Arial", 12, "bold"),
    bg="white"
).pack()



input_rail = tk.Entry(
    frame,
    width=15,
    font=("Arial", 12)
)

input_rail.pack(
    pady=10
)



# BUTTON

btn = tk.Frame(
    app,
    bg="#DDF3FF"
)

btn.pack(
    pady=5
)



tk.Button(
    btn,
    text="🔒 ENKRIPSI",
    width=14,
    height=2,
    bg="#27AE60",
    fg="white",
    font=("Arial",10,"bold"),
    command=enkripsi
).grid(
    row=0,
    column=0,
    padx=8
)



tk.Button(
    btn,
    text="🔓 DEKRIPSI",
    width=14,
    height=2,
    bg="#8E44AD",
    fg="white",
    font=("Arial",10,"bold"),
    command=dekripsi
).grid(
    row=0,
    column=1,
    padx=8
)



tk.Button(
    btn,
    text="🔄 RESET",
    width=14,
    height=2,
    bg="#F39C12",
    fg="white",
    font=("Arial",10,"bold"),
    command=reset
).grid(
    row=0,
    column=2,
    padx=8
)



# HASIL OUTPUT

tk.Label(
    app,
    text="✨ HASIL OUTPUT ✨",
    font=("Arial",15,"bold"),
    fg="#1769AA",
    bg="#DDF3FF"
).pack(
    pady=15
)



output = tk.Text(
    app,
    width=50,
    height=4,
    font=("Arial",11),
    bg="white",
    fg="black"
)

output.pack()



footer = tk.Label(
    app,
    text="Plaintext → Ciphertext\nCiphertext → Plaintext",
    font=("Arial",10),
    bg="#DDF3FF"
)

footer.pack(
    pady=15
)



app.mainloop()