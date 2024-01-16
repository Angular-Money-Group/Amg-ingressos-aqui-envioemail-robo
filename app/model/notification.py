class Notification(object):
    def __init__(self, _id, Sender, To, Subject, Attachments, Body, Type, Status,DateRegistration,DateSending):
        self._id = _id
        self.Sender = Sender
        self.To = To
        self.Subject = Subject
        self.Attachments = Attachments
        self.Body = Body
        self.Type = Type
        self.Status = Status
        self.DateRegistration = DateRegistration
        self.DateSending = DateSending