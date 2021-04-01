import converters

graphics = {
    "geforce": "GeForce",
    "nvidia": "Nvidia"
}

gpu = str(input("GPU Type: "))
try:
    weight = float(input("Weight: "))
except ValueError:
    print('Please input a number.')
    exit()
metric = input("(L)bs or (K)g: ")

if metric.lower() == 'l':
    metric = 'lbs'
    choice = input("Would you like to convert to kg? (Y or N): ")
    if choice.lower() == 'y':
        weight = converters.lbs_to_kg(weight)
        metric = 'kg'
elif metric.lower() == 'k':
    metric = 'kg'
    choice = input("Would you like to convert to lbs? (Y or N): ")
    if choice.lower() == 'y':
        weight = converters.kg_to_lbs(weight)
        metric = 'lbs'

model = input("Model: ")
try:
    cpufreq = int(input("CPU Frequency: "))
except ValueError:
    print('Please input a number.')
    exit()
cpu_metric = input("(G)hz or (M)hz: ")

if cpu_metric.lower() == 'g':
    cpu_metric = "GHz"
    if input("Would you like to convert to MHz? (Y or N): ").lower() == 'y':
        cpufreq = converters.ghz_to_mhz(cpufreq)
        cpu_metric = "MHz"
elif cpu_metric.lower() == 'm':
    cpu_metric = 'MHz'
    if input("Would you like to convert to GHz? (Y or N): ").lower() == 'y':
        cpufreq = converters.mhz_to_ghz(cpufreq)
        cpu_metric = "GHz"
    

gpu = gpu.lower()


if gpu in graphics: # fixed
    gpu = graphics.get(gpu)
    output = f'{cpufreq}{cpu_metric} {gpu} {weight}{metric} {model}'
    cpu = f'CPU Speed: {str(cpufreq)}{cpu_metric}'
    model = f'Model: {model}'
    weight = f'Weight: {weight}{metric}'
    gpu = f'GPU Type: {gpu}'
    
    print(f'''
{cpu}
{weight}
{gpu}
{model}
{output}
    ''') # fixed
else:
  print('Please input either GeForce or Nvidia.')