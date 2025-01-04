from modeltranslation.translator import translator, TranslationOptions
from .models import Doctor, PatientProfile, Appointment, Feedback, MedicalRecord


class DoctorTranslationOptions(TranslationOptions):
    fields = ('speciality', 'department')


class PatientProfileTranslationOptions(TranslationOptions):
    fields = ('blood_type',)


class AppointmentTranslationOptions(TranslationOptions):
    fields = ('status',)


class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)


class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')



translator.register(Doctor, DoctorTranslationOptions)
translator.register(PatientProfile, PatientProfileTranslationOptions)
translator.register(Appointment, AppointmentTranslationOptions)
translator.register(Feedback, FeedbackTranslationOptions)
translator.register(MedicalRecord, MedicalRecordTranslationOptions)

