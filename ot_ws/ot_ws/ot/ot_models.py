class Event(object):
    def __init__(self):
        self.folder = r'01. ITSM - Service Operation\01. Event Management'
        self.requiredfields = []
        self.fields = {
            "Answers": "TimeStampedMemoVal",
            "Applicant": "ReferenceToUserVal",
            "AssociatedBmsJobExecs": "ReferenceListVal",
            "AssociatedCI": "NullVal",
            "AssociatedCategory": "NullVal",
            "AssociatedClosureCategory": "NullVal",
            "AssociatedExternalPersons": "ReferenceListVal",
            "Attachments": "AttachmentsVal",
            "CINumber": "NullVal",
            "Call Finished Date": "DateTimeVal",
            "Call Status": "NullVal",
            "Class": "StringVal",
            "CorrelatedEvents": "ReferenceListVal",
            "CountCorrelatedEvents": "LongIntVal",
            "CountEventMails": "LongIntVal",
            "CreationDate": "DateTimeVal",
            "Description": "NullVal",
            "EventID": "NullVal",
            "Eventaction": "NullVal",
            "Eventsystem": "StringVal",
            "Eventtype": "ReferenceVal",
            "ExternalTickets": "ReferenceListVal",
            "Impact": "StringVal",
            "InitialAssociatedCategory": "NullVal",
            "LastChange": "DateTimeVal",
            "ManualSLAChange": "BoolVal",
            "Number": "LongIntVal",
            "Phone Number": "StringVal",
            "PickUpDateTime": "NullVal",
            "PreferredContactType": "StringVal",
            "Priority": "StringVal",
            "RelatedChange": "NullVal",
            "RelatedEmails": "ReferenceListVal",
            "RelatedIncident": "ReferenceVal",
            "RelatedProblem": "NullVal",
            "Reopened": "BoolVal",
            "ReportingCompany": "NullVal",
            "Responsible": "ReferenceToUserVal",
            "Source": "StringVal",
            "State": "StringVal",
            "Subclass": "StringVal",
            "TIGGroup": "NullVal",
            "Title": "NullVal",
            "TransferHistory": "StringVal",
            "UCID": "StringVal",
            "UCOnSiteBreachReason": "NullVal",
            "UCResolutionBreachReason": "NullVal",
            "UCResponseBreachReason": "NullVal",
            "Urgency": "StringVal"
        }


class Ticket(object):
    def __init__(self):
        self.folder = r'01. ITSM - Service Operation\02. Incident Management'
        self.requiredfields = ["Title", "Description", "AssociatedCategory"]
        self.fields = {
            "AffectedCMDBCIs": "ReferenceListVal",
            "AllActivitiesClosed": "BoolVal",
            "Answers": "TimeStampedMemoVal",
            "Applicant": "ReferenceToUserVal",
            "Assessment-Comment": "TimeStampedMemoVal",
            "Assessment-Quality": "NullVal",
            "Assessment-Time": "NullVal",
            "AssociatedActivities": "ReferenceListVal",
            "AssociatedBmsJobExecs": "ReferenceListVal",
            "AssociatedCategory": "ReferenceVal",
            "AssociatedCategoryChanged": "BoolVal",
            "AssociatedClosureCategory": "ReferenceVal",
            "AssociatedContract": "NullVal",
            "AssociatedExternalPersons": "ReferenceListVal",
            "AssociatedServiceRequest": "NullVal",
            "AssociatedStandardSolution": "NullVal",
            "Attachments": "AttachmentsVal",
            "CausedBy": "NullVal",
            "Class": "StringVal",
            "ClosureCode": "ReferenceVal",
            "CodeClientID": "NullVal",
            "CountClosedActivities": "ShortIntVal",
            "CountTotalActivities": "ShortIntVal",
            "CreatedFromRequest": "BoolVal",
            "CreationDate": "DateTimeVal",
            "Description": "StringVal",
            "EscalationsEnabled": "BoolVal",
            "ExternalComment": "NullVal",
            "ExternalCompany": "NullVal",
            "ExternalEmailAddress": "NullVal",
            "ExternalTicketNumber": "NullVal",
            "ExternalTickets": "ReferenceListVal",
            "FirstCallResolution": "BoolVal",
            "From Email Adress": "NullVal",
            "GrandTotalActivies": "NullVal",
            "Impact": "StringVal",
            "InitialAssociatedCategory": "ReferenceVal",
            "LastChange": "DateTimeVal",
            "ManualSLAChange": "BoolVal",
            "MvClosedFolder": "BoolVal",
            "Number": "LongIntVal",
            "OnSiteEnabled": "BoolVal",
            "OnSiteResponseDate1": "NullVal",
            "OnSiteResponseDate2": "NullVal",
            "OnSiteResponseDate3": "NullVal",
            "OnSiteResponseTargetDate": "NullVal",
            "OnSiteSLAState": "StringVal",
            "OnSiteSLAStopped": "BoolVal",
            "OnSiteSLAStoppedData": "NullVal",
            "PreferredContactType": "StringVal",
            "Priority": "StringVal",
            "Project": "NullVal",
            "RealResolutionTime": "NullVal",
            "RealResponseTime": "NullVal",
            "RelatedEGuichet": "ReferenceListVal",
            "RelatedEmails": "ReferenceListVal",
            "RelatedEvents": "ReferenceListVal",
            "RelatedMasterIncident": "NullVal",
            "RelatedProblem": "NullVal",
            "RelatedRFC": "NullVal",
            "RelatedSlaveIncidents": "ReferenceListVal",
            "Reopened": "BoolVal",
            "ReportingCompany": "ReferenceVal",
            "ReportingCostcenter": "NullVal",
            "ReportingLocation": "ReferenceVal",
            "ReportingPerson": "ReferenceVal",
            "RequestType": "StringVal",
            "ResolutionDate1": "NullVal",
            "ResolutionDate2": "NullVal",
            "ResolutionDate3": "NullVal",
            "ResolutionEnabled": "BoolVal",
            "ResolutionSLAState": "StringVal",
            "ResolutionSLAStopped": "BoolVal",
            "ResolutionSLAStoppedDate": "DateTimeVal",
            "ResolutionTargetDate": "NullVal",
            "ResponseDate1": "NullVal",
            "ResponseDate2": "NullVal",
            "ResponseDate3": "NullVal",
            "ResponseEnabled": "BoolVal",
            "ResponseSLAState": "StringVal",
            "ResponseSLAStopped": "BoolVal",
            "ResponseSLAStoppedDate": "DateTimeVal",
            "ResponseTargetDate": "NullVal",
            "Responsible": "ReferenceToUserVal",
            "SolutionDescription": "StringVal",
            "Source": "StringVal",
            "State": "StringVal",
            "Subclass": "StringVal",
            "SupportTimePeriod": "ReferenceVal",
            "TIGGroup": "ReferenceVal",
            "TimeInGroups": "ReferenceListVal",
            "TimeSpent": "NullVal",
            "Title": "StringVal",
            "UCOnSiteBreachReason": "NullVal",
            "UCResolutionBreachReason": "NullVal",
            "UCResponseBreachReason": "NullVal",
            "Urgency": "StringVal",
            "WV": "NullVal",
            "Waittime": "LongIntVal"
        }


class Agent(object):
    def __init__(self):
        self.folder = r'01. ITSM - Service Operation\02. Incident Management'
        self.requiredfields = ["FirstName",
                               "LastName", "Login Name", "displayname"]
        self.fields = {
            "AcademicTitle": "NullVal",
            "Active": "BoolVal",
            "AssociatedCostcenters": "ReferenceListVal",
            "Locations": "ReferenceListVal",
            "Applicant": "ReferenceToUserVal",
            "AssignToAllLocations": "BoolVal",
            "Attachments": "AttachmentsVal",
            "Authentication": "StringVal",
            "Birthday": "NullVal",
            "BirthdayReminder": "BoolVal",
            "Calendar": "NullVal",
            "Class": "StringVal",
            "AssociatedCIs": "ReferenceListVal",
            "Answers": "TimeStampedMemoVal",
            "Company": "ReferenceVal",
            "ContainedInGroups": "ReferenceListVal",
            "CreationDate": "DateTimeVal",
            "Department": "StringVal",
            "Description": "StringVal",
            "Email Address": "StringVal",
            "Fax": "NullVal",
            "FirstName": "StringVal",
            "Gender": "StringVal",
            "IdleSince": "NullVal",
            "InternalNumber": "NullVal",
            "LastChange": "DateTimeVal",
            "LastLogin": "DateTimeVal",
            "LastName": "StringVal",
            "LDAP Profile": "NullVal",
            "Locked": "BoolVal",
            "MainCostCenter": "NullVal",
            "Location": "ReferenceVal",
            "MobilePhone": "StringVal",
            "Number": "LongIntVal",
            "Password": "NullVal",
            "PersonnelRecord": "NullVal",
            "Phone": "StringVal",
            "Primary Group": "ReferenceVal",
            "Priority": "StringVal",
            "Properties": "NullVal",
            "RefOTUser": "ReferenceToUserVal",
            "RelatedEmails": "ReferenceListVal",
            "BirthdayRemindDate": "NullVal",
            "Responsible": "ReferenceToUserVal",
            "ResubmissionEnabled": "BoolVal",
            "ResubmissionDate": "NullVal",
            "ResubmissionEmail": "NullVal",
            "ResubmissionReason": "NullVal",
            "ResubmissionText": "NullVal",
            "ResubmissionUser": "ReferenceToUserVal",
            "JobTitle": "NullVal",
            "Salutation": "StringVal",
            "State": "StringVal",
            "Subclass": "StringVal",
            "Superuser": "BoolVal",
            "Title": "StringVal",
            "Login Name": "StringVal",
            "Type": "StringVal",
            "IsVIP": "BoolVal",
            "WebGuestPassword": "NullVal",
            "WebGuestUserName": "NullVal",
            "Windows Domain Name": "StringVal"
        }


class Category(object):
    def __init__(self):
        self.folder = r'01.ITSM - Categories'
        self.requiredfields = ["Title", "Predecessor", "SearchCode"]
        self.fields = {
            "ActivitiesIncident": "ReferenceListVal",
            "ActivitiesProblem": "ReferenceListVal",
            "ActivitiesRequest": "ReferenceListVal",
            "ActivitiesRfC": "ReferenceListVal",
            "Applicant": "ReferenceToUserVal",
            "Attachments": "AttachmentsVal",
            "Class": "StringVal",
            "Answers": "TimeStampedMemoVal",
            "CreationDate": "DateTimeVal",
            "Description": "NullVal",
            "Imported": "BoolVal",
            "KB-Subscription": "ReferenceListVal",
            "LastChange": "DateTimeVal",
            "Number": "LongIntVal",
            "Path": "StringVal",
            "Predecessor": "ReferenceVal",
            "Responsible": "ReferenceToUserVal",
            "ResponsibleIncident": "ReferenceToUserVal",
            "ResponsibleProblem": "ReferenceToUserVal",
            "ResponsibleRFC": "ReferenceToUserVal",
            "ResponsibleRequest": "ReferenceToUserVal",
            "SearchCode": "StringVal",
            "ServiceCatalogue": "ReferenceListVal",
            "StandardImpact": "StringVal",
            "StandardPriority": "StringVal",
            "StandardUrgency": "StringVal",
            "State": "StringVal",
            "Successors": "ReferenceListVal",
            "Title": "StringVal"
        }
