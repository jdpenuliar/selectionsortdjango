from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp
    return array 

def indexMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for count in range (minIndex, len(array)):
        if array[count] < minValue: 
            minIndex = count 
            minValue = array[count]
    return minIndex

def sort(request):
    array = []
    if request.method == "POST":
        for count in range (0, len(request.POST['array'])):
            print ("haha----\n", request.POST["array"][count])
            if (request.POST["array"][count] != ","):
                if (request.POST["array"][count] == "-"):
                    continue
                elif ((request.POST["array"][count - 1] == "-" and count == 1) or request.POST["array"][count - 2] == "-"):
                    array.append(int(request.POST["array"][count]) * -1) 
                else:
                    array.append(int(request.POST["array"][count])) 

        print ("array----\n", array)
        for x in range (0, len(array)):
            y = indexMinimum(array, x)
            swap(array, x, y)

        print ("array-----\n", array)

    return redirect('/') 

def index(request):
    return render(request, 'selectionSort/index.html') 
