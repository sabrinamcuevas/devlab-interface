import hl7

def interpret_message(data):
    mensaje_hl7 = hl7.parse(data)
    data_extracted = {
        "patient_id": mensaje_hl7.segment("PID")[3][0],
        "results": mensaje_hl7.segment("OBX")[5][0]
    }
    print("Data extracted:", data_extracted)
    return data_extracted
