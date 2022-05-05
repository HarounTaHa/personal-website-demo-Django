from django.shortcuts import render, redirect

# Create your views here.
from portfolio.forms import ContactForm
from portfolio.models import Project, ProjectImage, Service, Testimonial, Contact


def index(request):
    form_contact = ContactForm()
    data_projects = []
    projects = Project.objects.all()
    for p in projects:
        collect_data = {}
        project_images = ProjectImage.objects.filter(project__pk=p.pk).values_list('image', flat=True).first()
        project_ids = ProjectImage.objects.filter(project__pk=p.pk).values_list('project_id', flat=True)
        data = Project.objects.filter(id__in=project_ids)
        collect_data.update({'project': data, 'images': project_images})

        data_projects.append(collect_data)

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    fetch_data = {'projects': data_projects, 'services': services, 'testimonials': testimonials, 'form': form_contact}
    return render(request, 'portfolio/index.html', context=fetch_data)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            Contact.objects.create(name=name, email=email, message=message)
        except:
            return redirect('portfolio:index')
        return redirect('portfolio:index')


def project_details(request, pk):
    project_images = ProjectImage.objects.filter(project__pk=pk).values_list('image', flat=True)
    project = Project.objects.get(pk=pk)
    contex = {'project': project, 'project_images': project_images}
    return render(request, 'portfolio/project-details.html', context=contex)


def service_details(request, pk):
    service = Service.objects.get(pk=pk)
    contex = {'service': service}
    return render(request, 'portfolio/inner-page.html', context=contex)
