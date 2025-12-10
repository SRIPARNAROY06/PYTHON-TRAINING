import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle
from django.core.exceptions import ValidationError


def vehicles_list(request):

    if request.method == "GET":
        vehicles = list(Vehicle.objects.values())
        return JsonResponse(vehicles, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)


def vehicle_detail(request, id):

    try:
        vehicle = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        return JsonResponse({"error": "Vehicle not found"}, status=404)

    if request.method == "GET":
        data = {
            "id": vehicle.id,
            "number_plate": vehicle.number_plate,
            "vehicle_type": vehicle.vehicle_type,
            "manufacturer": vehicle.manufacturer,
            "year": vehicle.year,
            "created_at": vehicle.created_at,
            "updated_at": vehicle.updated_at,
        }
        return JsonResponse(data)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def create_vehicle(request):

    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    required = ["number_plate", "vehicle_type", "manufacturer", "year"]
    for field in required:
        if field not in data:
            return JsonResponse({"error": f"Missing field: {field}"}, status=400)

    # Basic validations
    try:
        year = int(data["year"])
        if year < 1886 or year > 3000:  # 1886 = earliest automobile year (safe guard)
            return JsonResponse({"error": "Invalid year value"}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Year must be an integer"}, status=400)

    try:
        veh = Vehicle.objects.create(
            number_plate=data["number_plate"].strip().upper(),
            vehicle_type=data["vehicle_type"].strip(),
            manufacturer=data["manufacturer"].strip(),
            year=year
        )
    except Exception as e:
        # Unique constraint or other DB error
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Vehicle created", "id": veh.id}, status=201)


@csrf_exempt
def update_vehicle(request, id):

    if request.method != "PUT":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        veh = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        return JsonResponse({"error": "Vehicle not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if "number_plate" in data:
        veh.number_plate = data["number_plate"].strip().upper()
    if "vehicle_type" in data:
        veh.vehicle_type = data["vehicle_type"].strip()
    if "manufacturer" in data:
        veh.manufacturer = data["manufacturer"].strip()
    if "year" in data:
        try:
            year = int(data["year"])
            if year < 1886 or year > 3000:
                return JsonResponse({"error": "Invalid year value"}, status=400)
            veh.year = year
        except (ValueError, TypeError):
            return JsonResponse({"error": "Year must be an integer"}, status=400)

    try:
        veh.save()
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Vehicle updated"})


@csrf_exempt
def delete_vehicle(request, id):

    if request.method != "DELETE":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    try:
        veh = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        return JsonResponse({"error": "Vehicle not found"}, status=404)

    veh.delete()
    return JsonResponse({"message": "Vehicle deleted"})


