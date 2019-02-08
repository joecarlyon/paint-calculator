import math
import re

from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/v1/calculate', methods=['POST'])
def calculate():
    data = request.json
    formatted_data = {}
    total_gallons_required = 0

    for room_number, room_data in data.items():
        formatted_data[room_number] = {}
        formatted_data[room_number]['ft'] = calculate_feet(room_data)
        formatted_data[room_number]['gallons'] = calculate_gallons_required(formatted_data[room_number])
        formatted_data[room_number]['room'] = re.search(r'(\d+)$', room_number).group(0)
        total_gallons_required += formatted_data[room_number]['gallons']
    formatted_data['total_gallons'] = total_gallons_required
    return jsonify(formatted_data)


def calculate_feet(formatted_data):
    """
    Calculate the number of feet required to paint the surface area of a single room
    :param formatted_data: dict of L/W/H information
    :return: integer for the number of feet required by performing `((Length * 2) + (Width * 2)) * Height`
    """
    return int(formatted_data['length']) * int(formatted_data['width']) * int(formatted_data['height'])


def calculate_gallons_required(formatted_data):
    """
    Number of feet to paint divided by the amount of feet the paint will cover, rounded up
    :param formatted_data: An integer for the number of feet required to paint
    :return: feet / paint coverage, rounded up
    """
    return math.floor(formatted_data['ft'] / 350)


def sanitize_input(input):
    """
    This universe doesn't allow for negative numbers of rooms or feet
    :param input: Any number
    :return: The absolute, integer number
    """
    return abs(int(input))
