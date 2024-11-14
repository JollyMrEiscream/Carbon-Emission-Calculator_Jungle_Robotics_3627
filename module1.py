elec_factor = {'coal':935, 'natural gas':500, 'oil':800, 'biomass':60, 'wind':11, 'solar power':45, 'hydropower':15, 'nuclear':15}
materials_factor = {'plastic':2.7, 'rubber':3.5, 'aluminum':12, 'steel':2.15, 'polycarbonate':7.35, 'copper wires':4.25}
transportation_factor = {'gasoline cars':185, 'diesel cars':150, 'hybrid cars':85, 'ev':0, 'diesel bus':1000, 'natural gas buses':850, 'electrical bus':0}
#waste_factor = 700

print("This is a wonderful carbon emissions calculator.")

# Electricity Emissions
elec_kind = input("What kind of energy did we use? Coal, Natural Gas, Oil, Biomass, Wind, Solar power, Hydropower, Nuclear: ").strip().lower()
electricity_consumption = input("How many kWh of electricity did we use?: ").strip()
elec_emi = elec_factor.get(elec_kind, 0) * int(electricity_consumption)


# Materials Emissions
material_kind = input("What materials did we use this year? Please do not use any spaces, but use commas to separate each material. Plastic, Rubber, Aluminum, Steel, Polycarbonate, Copper Wires:  ").lower()
material_kind = [x.strip() for x in material_kind.split(',')]
material_em_list = []

for material in material_kind:
    if material in materials_factor:
        quantity = input(f"How much of {material} did you use (in kilograms)?: ").strip()
        material_emission = materials_factor[material] * float(quantity)
        material_em_list.append(material_emission)
    else:
        print(f"Material '{material}' not found in materials_factor dictionary.")

total_material_emissions = sum(material_em_list)


# Transportation Emissions
transport_type = input("What type of transportation did we use? Gasoline cars, Diesel cars, Hybrid cars, EV, Diesel bus, Natural gas buses, Electrical bus: ").strip().lower()
distance_traveled = input(f"How many kilometers did we travel using {transport_type}?: ").strip()
transport_emi = transportation_factor.get(transport_type, 0) * float(distance_traveled)


# Waste Emissions
#waste_quantity = input("How much waste did we generate (in kilograms)?: ").strip()
#waste_emi = waste_factor * float(waste_quantity)


# Total Emissions
total_emissions = elec_emi + total_material_emissions + transport_emi
print(f"The total carbon emissions are {total_emissions} kg CO2.")
