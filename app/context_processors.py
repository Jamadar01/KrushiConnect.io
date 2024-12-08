from app.models import Contact, Medicines, ProductItems, MyOrders, Sell, FarmerProfile, customerProfile

def user_role_processor(request):
    user_role = None
    farmer_role = None
    
    if request.user.is_authenticated:
        try:
            # Get the customer profile and assign the role
            customer = customerProfile.objects.get(user=request.user)
            user_role = getattr(customer, 'role', None)
        except customerProfile.DoesNotExist:
            user_role = None

        try:
            # Get the farmer profile and assign the role
            farmer = FarmerProfile.objects.get(user=request.user)
            farmer_role = getattr(farmer, 'role', None)
        except FarmerProfile.DoesNotExist:
            farmer_role = None

    return {
        'user_role': user_role,
        'farmer_role': farmer_role,
    }
