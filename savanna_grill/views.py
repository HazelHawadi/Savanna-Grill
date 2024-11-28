from django.shortcuts import render, redirect
from django.http import HttpResponse
from menu.models import Category, MenuItem  # Import from the menu app
from django.contrib.auth.decorators import login_required
from .models import Review 

def home(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'home.html', {'categories': categories})  # Pass categories to the template

# Submit review view
@login_required
def submit_review(request):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        rating = request.POST.get('rating') 

        if not review_text or not rating:  # Check if the required fields are filled
            return HttpResponse("Review text and rating are required.", status=400) 

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