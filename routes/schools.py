from flask import Blueprint, jsonify
from models.models import School, db

schools_bp = Blueprint('schools', __name__)

@schools_bp.route('/api/schools', methods=['GET'])
def get_schools():
    try:
        schools = School.query.all()
        return jsonify([school.to_dict() for school in schools]), 200
    except Exception as e:
        schools_bp.logger.error(f"获取学校列表失败: {str(e)}")
        return jsonify({'error': f'获取学校列表失败: {str(e)}'}), 500