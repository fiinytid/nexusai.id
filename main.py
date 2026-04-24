from fasthtml.common import *

# Deklarasi ini SANGAT PENTING untuk Vercel
# Vercel akan membaca variabel 'app' dari baris ini
app, rt = fast_app()

@rt('/')
def get():
    return Titled("NEXUS AI Dashboard", 
        p("Selamat datang di NEXUS AI!")
    )

# Catatan: Vercel tidak membutuhkan serve() di baris paling bawah, 
# tapi jika ada serve() biasanya tidak masalah karena Vercel akan mengabaikannya.
