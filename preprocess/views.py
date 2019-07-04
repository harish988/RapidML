from django.shortcuts import render

def index(request):
    print("hello")
    csv_file = request.FILES["myfile"]
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    df = []
    field_names = lines[0].split(",")
    print(field_names)

    context = {
        'header':field_names
    }
    return render(request, 'preprocess/index.html', context)