
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEATTRIB COMMA DIVIDE FUNC ID IF LBR LPAREN LT MINUS NUMBER PLUS RBR RETURN RPAREN SEMICOLON TIMES WHILEfunctions : function functions\n                | empty\n    function : FUNC ID LPAREN params RPAREN LBR statements RBRparams : ID plist plist : COMMA ID plist\n             | empty\n    statements : statement statements\n                | empty\n    statement : attrib\n                | if\n                | while\n                | return\n                empty : if : IF LPAREN logic RPAREN LBR statements RBRwhile : WHILE LPAREN logic RPAREN LBR statements RBRreturn : RETURN logic SEMICOLONattrib : ID ATTRIB logic SEMICOLONlogic : logic LT logiclogic : expressionexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : termterm : term TIMES termterm : term DIVIDE termterm : NUMBERterm : IDterm : LPAREN expression RPAREN'
    
_lr_action_items = {'FUNC':([0,2,29,],[4,4,-3,]),'$end':([0,1,2,3,5,29,],[-13,0,-13,-2,-1,-3,]),'ID':([4,7,11,15,19,21,22,23,24,27,28,31,32,38,42,43,44,45,46,47,49,58,59,62,63,],[6,8,14,17,17,-9,-10,-11,-12,37,37,37,37,37,-16,37,37,37,37,37,-17,17,17,-14,-15,]),'LPAREN':([6,25,26,27,28,31,32,38,43,44,45,46,47,],[7,31,32,38,38,38,38,38,38,38,38,38,38,]),'COMMA':([8,14,],[11,11,]),'RPAREN':([8,9,10,12,14,16,34,35,36,37,40,41,48,52,53,54,55,56,57,],[-13,13,-4,-6,-13,-5,-19,-22,-25,-26,50,51,57,-18,-20,-21,-23,-24,-27,]),'LBR':([13,50,51,],[15,58,59,]),'RBR':([15,18,19,20,21,22,23,24,30,42,49,58,59,60,61,62,63,],[-13,29,-13,-8,-9,-10,-11,-12,-7,-16,-17,-13,-13,62,63,-14,-15,]),'IF':([15,19,21,22,23,24,42,49,58,59,62,63,],[25,25,-9,-10,-11,-12,-16,-17,25,25,-14,-15,]),'WHILE':([15,19,21,22,23,24,42,49,58,59,62,63,],[26,26,-9,-10,-11,-12,-16,-17,26,26,-14,-15,]),'RETURN':([15,19,21,22,23,24,42,49,58,59,62,63,],[27,27,-9,-10,-11,-12,-16,-17,27,27,-14,-15,]),'ATTRIB':([17,],[28,]),'NUMBER':([27,28,31,32,38,43,44,45,46,47,],[36,36,36,36,36,36,36,36,36,36,]),'SEMICOLON':([33,34,35,36,37,39,52,53,54,55,56,57,],[42,-19,-22,-25,-26,49,-18,-20,-21,-23,-24,-27,]),'LT':([33,34,35,36,37,39,40,41,52,53,54,55,56,57,],[43,-19,-22,-25,-26,43,43,43,43,-20,-21,-23,-24,-27,]),'PLUS':([34,35,36,37,48,53,54,55,56,57,],[44,-22,-25,-26,44,-20,-21,-23,-24,-27,]),'MINUS':([34,35,36,37,48,53,54,55,56,57,],[45,-22,-25,-26,45,-20,-21,-23,-24,-27,]),'TIMES':([35,36,37,55,56,57,],[46,-25,-26,-23,-24,-27,]),'DIVIDE':([35,36,37,55,56,57,],[47,-25,-26,-23,-24,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'functions':([0,2,],[1,5,]),'function':([0,2,],[2,2,]),'empty':([0,2,8,14,15,19,58,59,],[3,3,12,12,20,20,20,20,]),'params':([7,],[9,]),'plist':([8,14,],[10,16,]),'statements':([15,19,58,59,],[18,30,60,61,]),'statement':([15,19,58,59,],[19,19,19,19,]),'attrib':([15,19,58,59,],[21,21,21,21,]),'if':([15,19,58,59,],[22,22,22,22,]),'while':([15,19,58,59,],[23,23,23,23,]),'return':([15,19,58,59,],[24,24,24,24,]),'logic':([27,28,31,32,43,],[33,39,40,41,52,]),'expression':([27,28,31,32,38,43,44,45,],[34,34,34,34,48,34,53,54,]),'term':([27,28,31,32,38,43,44,45,46,47,],[35,35,35,35,35,35,35,35,55,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> functions","S'",1,None,None,None),
  ('functions -> function functions','functions',2,'p_func','parser.py',30),
  ('functions -> empty','functions',1,'p_func','parser.py',31),
  ('function -> FUNC ID LPAREN params RPAREN LBR statements RBR','function',8,'p_function','parser.py',36),
  ('params -> ID plist','params',2,'p_params','parser.py',42),
  ('plist -> COMMA ID plist','plist',3,'p_plist','parser.py',49),
  ('plist -> empty','plist',1,'p_plist','parser.py',50),
  ('statements -> statement statements','statements',2,'p_s','parser.py',58),
  ('statements -> empty','statements',1,'p_s','parser.py',59),
  ('statement -> attrib','statement',1,'p_statement','parser.py',66),
  ('statement -> if','statement',1,'p_statement','parser.py',67),
  ('statement -> while','statement',1,'p_statement','parser.py',68),
  ('statement -> return','statement',1,'p_statement','parser.py',69),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',74),
  ('if -> IF LPAREN logic RPAREN LBR statements RBR','if',7,'p_if','parser.py',78),
  ('while -> WHILE LPAREN logic RPAREN LBR statements RBR','while',7,'p_while','parser.py',87),
  ('return -> RETURN logic SEMICOLON','return',3,'p_return','parser.py',99),
  ('attrib -> ID ATTRIB logic SEMICOLON','attrib',4,'p_attrib','parser.py',103),
  ('logic -> logic LT logic','logic',3,'p_logic','parser.py',113),
  ('logic -> expression','logic',1,'p_logic_expression','parser.py',117),
  ('expression -> expression PLUS expression','expression',3,'p_e','parser.py',121),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',125),
  ('expression -> term','expression',1,'p_expression_term','parser.py',130),
  ('term -> term TIMES term','term',3,'p_term','parser.py',134),
  ('term -> term DIVIDE term','term',3,'p_term_div','parser.py',140),
  ('term -> NUMBER','term',1,'p_term_number','parser.py',145),
  ('term -> ID','term',1,'p_term_id','parser.py',149),
  ('term -> LPAREN expression RPAREN','term',3,'p_paren','parser.py',159),
]
