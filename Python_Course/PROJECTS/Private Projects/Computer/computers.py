graphics = {
    "geforce": "GeForce",
    "nvidia": "Nvidia"
}

gpu = str(input())
weight = float(input())
model = input()
cpufreq = int(input())


gpu.lower()
if gpu in graphics:
    gpu = graphics.get(gpu)
    output = f'{cpufreq}MHz {gpu} {weight}kg {model}'
    cpu = f'CPU Speed: {str(cpufreq)}MHz'
    model = f'Model: {model}'
    weight = f'Weight: {weight}kg'
    gpu = f'GPU Type: {gpu}'
    print(cpu)
    print(weight)
    print(gpu)
    print(model)
    print(output)
else:
  print('Please input either GeForce or Nvidia.')
