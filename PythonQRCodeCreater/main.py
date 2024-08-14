import qrcode
code = qrcode.QRCode(version=1,
                     error_correction= qrcode.constants.ERROR_CORRECT_L,
                     box_size=120,
                     border=6)
code.add_data("neganwashere")
code.make(fit=True)
image = code.make_image(fill_color=(12,123,66),back_color="white")
image.save("qrcode.png")

#######