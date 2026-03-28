from menu.models import MenuItem

MenuItem.objects.all().delete()

# Breakfast
MenuItem.objects.create(name='Idly', category='Breakfast', price=20.00, image_url='https://images.unsplash.com/photo-1543779505-f0e7319860f2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Parotta', category='Breakfast', price=25.00, image_url='https://images.unsplash.com/photo-1551183053-bf91a1d81141?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Poori', category='Breakfast', price=30.00, image_url='https://images.unsplash.com/photo-1543353071-087092ec3939?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Puttu', category='Breakfast', price=35.00, image_url='https://images.unsplash.com/photo-1618221288166-403d815027b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Ven Pongal', category='Breakfast', price=40.00, image_url='https://images.unsplash.com/photo-1597045552773-5ea405f1f3a6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Dosa', category='Breakfast', price=45.00, image_url='https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Masal Dosa', category='Breakfast', price=50.00, image_url='https://images.unsplash.com/photo-1584270354949-29f5e02e6c09?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Onion Dosa', category='Breakfast', price=55.00, image_url='https://images.unsplash.com/photo-1601924582975-4aaf5c478867?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Normal Dosa', category='Breakfast', price=45.00, image_url='https://images.unsplash.com/photo-1504299177189-3e7d8328c075?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')

# Lunch
MenuItem.objects.create(name='White Rice', category='Lunch', price=60.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/plain-rice-recipe-1.jpg')
MenuItem.objects.create(name='Tomato Rice', category='Lunch', price=65.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/tomato-rice-recipe-1.jpg')
MenuItem.objects.create(name='Lemon Rice', category='Lunch', price=70.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/lemon-rice-recipe-1.jpg')
MenuItem.objects.create(name='Curd Rice', category='Lunch', price=75.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/curd-rice-recipe-1.jpg')
MenuItem.objects.create(name='Mint Rice (Pudina Rice)', category='Lunch', price=85.00, image_url='https://images.unsplash.com/photo-1570028804694-83bf4f3cd60a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')
MenuItem.objects.create(name='Coconut Rice', category='Lunch', price=80.00, image_url='https://images.unsplash.com/photo-1623170903766-273a35f7d201?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60')

# Dinner
MenuItem.objects.create(name='Parotta', category='Dinner', price=25.00, image_url='https://i.pinimg.com/736x/5a/5b/5c/5a5b5c8b8b8b8b8b8b8b8b8b8b8b8b8b.jpg')
MenuItem.objects.create(name='Dosa', category='Dinner', price=45.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/dosa-recipe-1.jpg')
MenuItem.objects.create(name='Omelet', category='Dinner', price=30.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/omelette-recipe-1.jpg')
MenuItem.objects.create(name='Idly', category='Dinner', price=20.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/idli-recipe-1.jpg')
MenuItem.objects.create(name='Chicken Fried Rice', category='Dinner', price=80.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/chicken-fried-rice-recipe-1.jpg')
MenuItem.objects.create(name='Egg Rice', category='Dinner', price=70.00, image_url='https://www.vegrecipesofindia.com/wp-content/uploads/2018/07/egg-fried-rice-recipe-1.jpg')