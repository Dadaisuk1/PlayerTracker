from django.shortcuts import render, redirect, get_object_or_404
from .models import Hero, Game
from .forms import HeroForm, GameForm

# READ - List all games
def game_list(request):
    games = Game.objects.all()
    return render(request, 'HeroApp/game_list.html', {'games': games})

# CREATE - Add a new game
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('game_list')  # Redirect to the game list page
    else:
        form = GameForm()
    return render(request, 'HeroApp/game_create.html', {'form': form})

# UPDATE - Edit an existing game
def game_update(request, game_id):  # Use game_id instead of id
    game = get_object_or_404(Game, game_id=game_id)  # Use game_id instead of id
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'HeroApp/game_form.html', {'form': form})

# DELETE - Remove a game
def game_delete(request, game_id):  # Use game_id instead of id
    game = get_object_or_404(Game, game_id=game_id)  # Use game_id instead of id
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'HeroApp/game_confirm_delete.html', {'game': game})

def landing_page(request):
    return render(request, 'HeroApp/landing_page.html')

# READ - List all heroes
def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'HeroApp/hero_list.html', {'heroes': heroes})

# CREATE - Add a new hero
def hero_create(request):
    if request.method == 'POST':
        form = HeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = HeroForm()
    return render(request, 'HeroApp/hero_form.html', {'form': form})

# UPDATE - Edit an existing hero
def hero_update(request, id):
    hero = get_object_or_404(Hero, id=id)
    if request.method == 'POST':
        form = HeroForm(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = HeroForm(instance=hero)
    return render(request, 'HeroApp/hero_form.html', {'form': form})

# DELETE - Remove a hero
def hero_delete(request, id):
    hero = get_object_or_404(Hero, id=id)
    if request.method == 'POST':
        hero.delete()
        return redirect('hero_list')
    return render(request, 'HeroApp/hero_confirm_delete.html', {'hero': hero})
