from osv import osv
from osv import fields

class contracts(osv.osv):

  _name = 'ascs.contracts'
  _description = 'ascs.contracts'
 
  _columns = {
      'name':fields.char('Contract Name', size=64, required=True),
      'customer_id':fields.many2one('res.partner','Customer',required=False,ondelete='set null'),
      'start_date':fields.date('Start Date', size=64, required=False, readonly=False), 
      'end_date':fields.date('End Date', size=64, required=False, readonly=False), 
      'comments':fields.text('Comments', size=64, required=False, readonly=False),
      'termsnconditions_id':fields.one2many('ascs.termsnconditions','contract_id','Person Details'),
      'contract_details_id':fields.one2many('ascs.contractdetails','contract_id','Contract Details')
    }
contracts()

class ascs_contractdetails(osv.osv):
  
    _name = 'ascs.contractdetails'
    _description='ascs.contractdetails'
    
    
    _columns={
              'name':fields.char('Contract Details', size=64, required=False),
              'product_id':fields.many2one('product.product','Facility Type',required=True,ondelete='set null'),
              'rate':fields.float('Rate',required=False),
              'contract_id':fields.many2one('ascs.contractdetails','Contract',required=True,ondelete='set null')
                         
              }


ascs_contractdetails()

class terms_conditions(osv.osv):
    _name='ascs.termsnconditions'
    _description='ascs.termsnconditions'
    
    
    _columns={
        'name':fields.char('Contract Terms', size=64, required=True),
        'contract_id':fields.many2one('ascs.contracts','Contract',required=False,ondelete='set null'),
              
              }
      
terms_conditions()