import csv
import os
cvs_path = os.path.join('..', 'Resources', 'employee_data.csv')
with open(cvs_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)

    csv_header = next(csv_reader)
    print(csv_header, '\n')
    # print(f'CSV Header: {csv_header}' '\n')

    
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
    
    
    ID = []
    full_name =  []
    first_name = []
    last_name = []
    date_of_birth = []
    dob = []
    ssn = []
    ssn_stars = []
    abbreviation = []
    
    for row in csv_reader:
        #print(row)
        ID.append(row[0])
        full_name = row[1].split(" ")   
        first_name.append(full_name[0])
        last_name.append(full_name[1])
        #print(full_name)
        date_of_birth = row[2].split("-")
        dob.append(date_of_birth[1] + "/" + date_of_birth[2] + "/" + date_of_birth[0])
        #print(dob)
        ssn=row[3].split("-")
        ssn_stars.append("***-**-" + ssn[2])
        abbreviation.append(us_state_abbrev)