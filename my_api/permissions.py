from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    """
        I replaced the has_permission 
        by permission.IsAdminUser in
        permission_mixins.py
    """
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

#     def has_permission(self, request, view):
#         if request.user.is_staff:
# " <app_name> (dot) ACTION_FOR_WHICH_PERMISSION_IS_REQUIRED_<modelName> " 
#             if request.user.has_perm("my_product.view_product"): # view --> Permission to view the model !
#                 return True
#             if request.user.has_perm("my_product.change_product"): # change --> Permission to update the model !
#                 return True
#             if request.user.has_perm("my_product.add_product"): # add --> Permission to add a new object in the model !
#                 return True
#             if request.user.has_perm("my_product.delete_product"): # delete --> Permission to delete the model !
#                 return True
            
#             return False

#         return False