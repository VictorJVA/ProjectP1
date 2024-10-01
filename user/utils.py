# utils.py
from .interfaces import IAppointmentService, IVetService, IReportService, IPetService
from Client_User.models import Appointment, Vet, Report, Pets, Medical_history

class AppointmentService(IAppointmentService):
    def get_appointment(self, appointment_id: int):
        return Appointment.objects.filter(appointment_id=appointment_id).first()
    
    def get_vet_appointments(self, vet_id: int):
        return Appointment.objects.filter(vet_id=vet_id)
    
    def update_appointment(self, appointment_id: int, accepted: bool):
        Appointment.objects.filter(pk=appointment_id).update(appointment_accepted=accepted)

class ReportService(IReportService):
    def get_report(self, appointment_id: int):
        return Report.objects.filter(appointement_id=appointment_id).order_by('-report_id').first()
    
    def create_report(self, appointment, medical_history):
        return Report.objects.create(appointement_id=appointment, medical_history_id=medical_history)