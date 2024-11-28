from django.shortcuts import render, redirect
from django.http import HttpResponse
from menu.models import Category, MenuItem  # Import from the menu app
from .models import Review 

def home(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'home.html', {'categories': categories})  # Pass categories to the template

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

    return render(request, 'submit_review.html')  # Render the form on GET request

# View all reviews
def view_reviews(request):
    reviews = Review.objects.all()  # Fetch all reviews
    return render(request, 'view_reviews.html', {'reviews': reviews})    