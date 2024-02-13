API paths to test


** Via the LittleLemon Static HTML content **
- Create a user (register): /register
- Login: /login
- Logout (POST): /logout
- See all menu items: restaurant/menu/items/
- See a single item: /restaurant/menu/items/<int:pk>
- Book a table / See all reservations: /restaurant/booking/
- See all reservations: /restaurant/reservations/

** API endpoints Via the Insomnia REST Client **
- Create a user (register) / see users: /auth/users/
- Obtain authentication token: auth/api-token-auth
- Login: /auth/token/login
- Logout: /auth/token/logout
- See all menu items: /api/menu/items/
- See a single item: /api/menu/items/<int:pk>
- Book a table / See all reservations: /api/booking
