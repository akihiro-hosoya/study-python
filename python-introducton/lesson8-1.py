# coding:utf-8

# クラスのインポート
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicordCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

# フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

# pdfを作る
pdf = canvas.Canvas('example.pdf', pafesize=pagesizes.A4)
pdf.setFont('HeiseiKakuGo-W5', 14)
pdf.drawString(10 * Unit.mm, 270 * unit.mm, '初めてのPDF')
pdf.save()