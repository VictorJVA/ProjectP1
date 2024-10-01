from abc import ABC, abstractmethod

class IAppointmentService(ABC):
    @abstractmethod
    def get_appointment(self, appointment_id: int):
        pass
    
    @abstractmethod
    def get_vet_appointments(self, vet_id: int):
        pass
    
    @abstractmethod
    def update_appointment(self, appointment_id: int, accepted: bool):
        pass

class IReportService(ABC):
    @abstractmethod
    def get_report(self, appointment_id: int):
        pass
    
    @abstractmethod
    def create_report(self, appointment, medical_history):
        pass
