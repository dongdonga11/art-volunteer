from flask import Blueprint, request, jsonify
from models.models import Volunteer, School, db

volunteers_bp = Blueprint('volunteers', __name__)

@volunteers_bp.route('/api/volunteers', methods=['POST'])
def create_volunteer():
    try:
        data = request.get_json()
        
        # 验证必要字段
        if not all(k in data for k in ('school_id', 'user_id')):
            return jsonify({'error': '缺少必要字段'}), 400
            
        # 验证school_id是否存在
        school = School.query.get(data['school_id'])
        if not school:
            return jsonify({'error': '学校ID不存在'}), 404
            
        volunteer = Volunteer(
            school_id=data['school_id'],
            user_id=data['user_id'],
            priority=data.get('priority', False)
        )
        
        db.session.add(volunteer)
        db.session.commit()
        
        return jsonify(volunteer.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        volunteers_bp.logger.error(f"创建志愿失败: {str(e)}")
        return jsonify({'error': f'创建志愿失败: {str(e)}'}), 500

@volunteers_bp.route('/api/volunteers/<int:id>', methods=['PUT'])
def update_volunteer(id):
    try:
        volunteer = Volunteer.query.get(id)
        if not volunteer:
            return jsonify({'error': '志愿不存在'}), 404
            
        volunteer.priority = not volunteer.priority
        db.session.commit()
        
        return jsonify(volunteer.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        volunteers_bp.logger.error(f"更新志愿失败: {str(e)}")
        return jsonify({'error': f'更新志愿失败: {str(e)}'}), 500

@volunteers_bp.route('/api/volunteers/<int:id>', methods=['DELETE'])
def delete_volunteer(id):
    try:
        volunteer = Volunteer.query.get(id)
        if not volunteer:
            return jsonify({'error': '志愿不存在'}), 404
            
        db.session.delete(volunteer)
        db.session.commit()
        
        return jsonify({'message': '删除成功'}), 200
        
    except Exception as e:
        db.session.rollback()
        volunteers_bp.logger.error(f"删除志愿失败: {str(e)}")
        return jsonify({'error': f'删除志愿失败: {str(e)}'}), 500 