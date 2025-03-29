DATES = [('January',[31]),('February',[28,29]),('March',[31]),
('April',[30]),('May',[31]),('June',[30]),('July',[31]),
('August',[31]),('September',[30]),('October',[31]),
('November',[30]),('December',[31])]

def daysInMonth(value):
  
  days = [date for month , date in DATES if month == value ]
  
  return days[0] if days else []


print(daysInMonth("December"))
print(daysInMonth("February"))