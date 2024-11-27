from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review  

def home(request):
    return render(request, 'home.html')

# Submit review view
def submit_review(request):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')  

        # Save the review
        Review.objects.create(
            review=review_text,
            rating=rating,
            user=request.user if request.user.is_authenticated else None
        )

        return redirect('home')

    return HttpResponse("Invalid request", status=400)