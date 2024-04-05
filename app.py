from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# Route for handling the form submission

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user inputs from the form
        num_people = float(request.form['num_people'])
        location = float(request.form['location'])

        # Perform the energy calculation
        energy_per_person = 550  # W per person per day
        energy_per_sqm = 550  # Wh per one sqm per day
        efficiency = 0.05  # Conversion efficiency

        volume_per_person = (num_people / location)
        energy_per_day = volume_per_person * energy_per_person

        area_per_person = (energy_per_day / (efficiency * energy_per_sqm) / 10000)

        area_proc = location * area_per_person / 100

        russia_regions = {
            "Central Federal District": 650,  # S of region in square kilometers
            "Southern Federal District": 747,  # S of region in square kilometers
            "Northwestern Federal District": 1664,  # S of region in square kilometers
            "Far Eastern Federal District": 6132,  # S of region in square kilometers
            "Siberian Federal District": 5418,  # S of region in square kilometers
            "Ural Federal District": 1928,  # S of region in square kilometers
            "Volga Federal District": 1378,  # S of region in square kilometers
            "Kaliningrad Oblast": 223,  # S of region in square kilometers
            "Belgorod Oblast": 153,  # S of region in square kilometers
            "Bryansk Oblast": 348,  # S of region in square kilometers
            "Vladimir Oblast": 298,  # S of region in square kilometers
            "Voronezh Oblast": 524,  # S of region in square kilometers
            "Ivanovo Oblast": 145,  # S of region in square kilometers
            "Kaluga Oblast": 298,  # S of region in square kilometers
            "Kostroma Oblast": 60,  # S of region in square kilometers
            "Kursk Oblast": 296,  # S of region in square kilometers
            "Lipetsk Oblast": 244,  # S of region in square kilometers
            "Moscow Oblast": 447,  # S of region in square kilometers
            "Orel Oblast": 244,  # S of region in square kilometers
            "Ryazan Oblast": 391,  # S of region in square kilometers
            "Smolensk Oblast": 500,  # S of region in square kilometers
            "Tambov Oblast": 340,  # S of region in square kilometers
            "Tver Oblast": 844,  # S of region in square kilometers
            "Tula Oblast": 257,  # S of region in square kilometers
            "Yaroslavl Oblast": 367,  # S of region in square kilometers
            "Moscow": 2561,  # S of region in square kilometers
            "St. Petersburg": 1439,  # S of region in square kilometers
            "Republic of Karelia": 180.5,  # S of region in square kilometers
            "Leningrad Oblast": 83900,  # S of region in square kilometers
            "Murmansk Oblast": 144900,  # S of region in square kilometers
            "Novgorod Oblast": 55600,  # S of region in square kilometers
            "Pskov Oblast": 55400,  # S of region in square kilometers
            "Republic of Adygea": 7899,  # S of region in square kilometers
            "Republic of Kalmykia": 7484,  # S of region in square kilometers
            "Krasnodar Krai": 75466,  # S of region in square kilometers
            "Astrakhan Oblast": 44700,  # S of region in square kilometers
            "Volgograd Oblast": 39900,  # S of region in square kilometers
            "Rostov Oblast": 100800,  # S of region in square kilometers
            "Republic of Dagestan": 50280,  # S of region in square kilometers
            "Republic of Ingushetia": 3620,  # S of region in square kilometers
            "Kabardino-Balkar Republic": 12860,  # S of region in square kilometers
            "Karachay-Cherkess Republic": 14200,  # S of region in square kilometers
            "Republic of North Ossetia – Alania": 8020,  # S of region in square kilometers
            "Chechen Republic": 19900,  # S of region in square kilometers
            "Stavropol Krai": 66900,  # S of region in square kilometers
            "Republic of Crimea": 26900,  # S of region in square kilometers
            "Sevastopol": 1100,  # S of region in square kilometers
            "Republic of Bashkortostan": 143600,  # S of region in square kilometers
            "Republic of Mari El": 23300,  # S of region in square kilometers
            "Republic of Mordovia": 26400,  # S of region in square kilometers
            "Republic of Tatarstan": 67800,  # S of region in square kilometers
            "Udmurt Republic": 42600,  # S of region in square kilometers
            "Chuvash Republic": 18300,  # S of region in square kilometers
            "Perm Krai": 160600,  # S of region in square kilometers
            "Kirov Oblast": 120800,  # S of region in square kilometers
            "Nizhny Novgorod Oblast": 76900,  # S of region in square kilometers
            "Orenburg Oblast": 124000,  # S of region in square kilometers
            "Penza Oblast": 43200,  # S of region in square kilometers
            "Samara Oblast": 53600,  # S of region in square kilometers
            "Saratov Oblast": 100200,  # S of region in square kilometers
            "Ulyanovsk Oblast": 37300,  # S of region in square kilometers
            "Kurgan Oblast": 71000,  # S of region in square kilometers
            "Sverdlovsk Oblast": 194800,  # S of region in square kilometers
            "Tyumen Oblast": 160100,  # S of region in square kilometers
            "Chelyabinsk Oblast": 87400,  # S of region in square kilometers
            "Kaliningrad": 223,
            "Africa": 30370,
            "Antarctica": 14000,
            "Asia": 43820,
            "Europe": 10180,
            "North America": 24490,
            "Oceania": 8520,
            "South America": 17840,
            "Amazon rainforest": 5500,
            "Arabian Peninsula": 3300,
            "Canadian Shield": 4850,
            "Gobi Desert": 1300,
            "Great Barrier Reef": 348.7,
            "Greenland ice sheet": 1645,
            "Himalayas": 2400,
            "Mediterranean Sea": 2500,
            "Sahara Desert": 9000,
            "The Alps": 192,
            "The Andes": 7090,
            "The Pacific Ocean": 63800
        }
        threshold = 100
        close_regions = []
        diff=''
        for region, area in russia_regions.items():
            if abs(area - area_proc) <= threshold :
                diff = float(100-(((abs(area - area_proc))/area)*100))

                close_regions.append(region)
                break
        area_regions = ''.join(close_regions)
        # Render the results page with the calculated values
        return render_template('first.html', num_people=num_people,
                               location=location,
                               energy_per_day=round((energy_per_day/1000),2),
                               area_per_person=round(area_per_person,2), area_proc=round(area_proc,2), area_regions=area_regions, diff=round(diff,5))
    else:
        return render_template('first.html')


if __name__ == '__main__':
    app.run(debug=True)
