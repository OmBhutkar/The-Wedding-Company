from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Package


@login_required
def package_list(request):
    """List all packages"""
    packages = Package.objects.filter(is_active=True)
    
    context = {
        'packages': packages,
    }
    
    return render(request, 'packages/package_list.html', context)


@login_required
def package_detail(request, pk):
    """Package detail view"""
    package = get_object_or_404(Package, pk=pk)
    services = package.services.all()
    
    context = {
        'package': package,
        'services': services,
    }
    
    return render(request, 'packages/package_detail.html', context)


