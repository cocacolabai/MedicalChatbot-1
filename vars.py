import os

ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN', None)
VERIFY_TOKEN = "Med"
#os.environ.get('VERIFY_TOKEN', None)
ACCESS_TOKEN_TEST = "EAARvRzP5StsBAIBGd2ixFgsD38M8lEpur3cTNwxrxrsAmB8KhQtkdeAtpWm8AUw8IMAat9DMzaZAyjx8iijcOZCgZBrl2hVBznt0Th8uxS1rC659eLtBLu1aeKrP48ZB58ZBSaDGhwn0BVVGaZATZAFXoeA9l2Yfm4p7RdWldXBLQZDZD"
#os.environ.get('TEST_ACCESS_TOKEN', None)

DOC_MAX_LENGTH = 8
TYPE_MESSAGE = 'message'
TYPE_MESSAGE_CODE = 1
TYPE_POSTBACK = 'postback'
TYPE_POSTBACK_CODE = 2

# Opciones para las opciones de Postback
OPTION_EMERGENCY_CALL = 'emergencia'
OPTION_MEDICAL_QUERY = 'consulta'
OPTION_DOCTOR_SELECTED = 'doctor'

# Opciones para los valores de Predicción
PREDICT_WELCOME = 'saludo'
PREDICT_SYMPTOM = 'sintoma'
PREDICT_FAREWELL = 'despedida'

# Valores para respuestas de Postback
CALL_REPLAY = "Llamando a Emergencia..."
QUERY_REPLAY = "De acuerdo, ¿Cuáles son tus síntomas?"
DOCTOR_REPLAY = "Bien has seleccionado al %s"