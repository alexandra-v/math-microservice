from flask import request
from flask_restx import Namespace, Resource, fields
from .helpers import OperationType, OpValidation


api = Namespace('operations', description='')

compute_op_dto = api.model('Compute an operation', {
    'op_type': fields.String(required=True, enum=[x.name for x in OperationType]),
    'operands': fields.List(fields.Float(required=True), required=True),
})

@api.route('/')
class Operation(Resource):
    @api.doc('do an operation')
    @api.expect(compute_op_dto, validate=True)
    def post(self):
        from .tasks import compute_the_operation
        op_type, operands = request.json['op_type'], request.json['operands']
        validate = OpValidation.get(op_type)
        if not validate or not validate(operands):
            return {"message": "Bad request"}, 400

        compute_the_operation.delay(op_type, operands)        
        return {"message": "The request was queued for processing"}, 202


    
