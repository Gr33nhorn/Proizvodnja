from reportlab.pdfgen import canvas
from models import Box
import qrcode
from reportlab.graphics.shapes import Drawing

b = Box(tip="newBox")
b.qr_koda()
c = canvas.Canvas("QR.pdf")
c.drawString(100, 750, "Welcome to Reportlab!")

d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
d.add()
c.save()


