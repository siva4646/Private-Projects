graphics = {
    "geforce": "GeForce",
    "nvidia": "Nvidia"
}

gpu = str(input())
weight = float(input())
model = input()
cpufreq = int(input())


gpu = gpu.lower()
print(gpu)
if gpu in graphics: # fixed
    gpu = graphics.get(gpu)
    output = f'{cpufreq}MHz {gpu} {weight}kg {model}'
    cpu = f'CPU Speed: {str(cpufreq)}MHz'
    model = f'Model: {model}'
    weight = f'Weight: {weight}kg'
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
