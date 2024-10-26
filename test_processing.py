from processing import interpret_message

def test_interpret_message():
    mensaje = "MSH|^~\\&|LAB|L||202401012359||ORU^R01|12345|P|2.4\rPID|||123456||Doe^John\rOBX|1|NM|WBC^Leucocitos||5.5|10^3/uL|4.0-10.0|N||F"
    data = interpret_message(mensaje)
    assert data["patient_id"] == "123456"
    assert data["results"] == "5.5"
