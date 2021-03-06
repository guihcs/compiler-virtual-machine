
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEATTRIB COMMA DIVIDE FUNC ID IF LBR LPAREN LT MINUS NUMBER PLUS RBR RETURN RPAREN SEMICOLON TIMES WHILEfunctions : function functions\n                | empty\n    function : FUNC ID LPAREN params RPAREN LBR statements RBRpcall : logic pclist\n             | empty\n     pclist : COMMA logic pclist\n             | empty\n    params : ID plist\n              | empty\n     plist : COMMA ID plist\n             | empty\n    statements : statement statements\n                | empty\n    statement : attrib\n                | if\n                | while\n                | return\n                empty : if : IF LPAREN logic RPAREN LBR statements RBRwhile : WHILE LPAREN logic RPAREN LBR statements RBRreturn : RETURN logic SEMICOLONattrib : ID ATTRIB logic SEMICOLONlogic : logic LT logiclogic : expressionexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : termterm : term TIMES termterm : term DIVIDE termterm : callterm : NUMBERterm : IDcall : ID LPAREN pcall RPAREN term : LPAREN expression RPAREN'
    
_lr_action_items = {'FUNC':([0,2,30,],[4,4,-3,]),'$end':([0,1,2,3,5,30,],[-18,0,-18,-2,-1,-3,]),'ID':([4,7,12,16,20,22,23,24,25,28,29,32,33,40,44,45,46,47,48,49,50,52,64,65,68,73,74,],[6,8,15,18,18,-14,-15,-16,-17,39,39,39,39,39,-21,39,39,39,39,39,39,-22,18,18,39,-19,-20,]),'LPAREN':([6,26,27,28,29,32,33,39,40,45,46,47,48,49,50,68,],[7,32,33,40,40,40,40,50,40,40,40,40,40,40,40,40,]),'RPAREN':([7,8,9,10,11,13,15,17,35,36,37,38,39,42,43,50,51,55,56,57,58,59,60,61,62,63,66,67,69,72,75,],[-18,-18,14,-9,-8,-11,-18,-10,-24,-27,-30,-31,-32,53,54,-18,63,-23,-25,-26,-28,-29,66,-18,-5,-34,-33,-4,-7,-18,-6,]),'COMMA':([8,15,35,36,37,38,39,55,56,57,58,59,61,63,66,72,],[12,12,-24,-27,-30,-31,-32,-23,-25,-26,-28,-29,68,-34,-33,68,]),'LBR':([14,53,54,],[16,64,65,]),'RBR':([16,19,20,21,22,23,24,25,31,44,52,64,65,70,71,73,74,],[-18,30,-18,-13,-14,-15,-16,-17,-12,-21,-22,-18,-18,73,74,-19,-20,]),'IF':([16,20,22,23,24,25,44,52,64,65,73,74,],[26,26,-14,-15,-16,-17,-21,-22,26,26,-19,-20,]),'WHILE':([16,20,22,23,24,25,44,52,64,65,73,74,],[27,27,-14,-15,-16,-17,-21,-22,27,27,-19,-20,]),'RETURN':([16,20,22,23,24,25,44,52,64,65,73,74,],[28,28,-14,-15,-16,-17,-21,-22,28,28,-19,-20,]),'ATTRIB':([18,],[29,]),'NUMBER':([28,29,32,33,40,45,46,47,48,49,50,68,],[38,38,38,38,38,38,38,38,38,38,38,38,]),'SEMICOLON':([34,35,36,37,38,39,41,55,56,57,58,59,63,66,],[44,-24,-27,-30,-31,-32,52,-23,-25,-26,-28,-29,-34,-33,]),'LT':([34,35,36,37,38,39,41,42,43,55,56,57,58,59,61,63,66,72,],[45,-24,-27,-30,-31,-32,45,45,45,45,-25,-26,-28,-29,45,-34,-33,45,]),'PLUS':([35,36,37,38,39,51,56,57,58,59,63,66,],[46,-27,-30,-31,-32,46,-25,-26,-28,-29,-34,-33,]),'MINUS':([35,36,37,38,39,51,56,57,58,59,63,66,],[47,-27,-30,-31,-32,47,-25,-26,-28,-29,-34,-33,]),'TIMES':([36,37,38,39,58,59,63,66,],[48,-30,-31,-32,-28,-29,-34,-33,]),'DIVIDE':([36,37,38,39,58,59,63,66,],[49,-30,-31,-32,-28,-29,-34,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'functions':([0,2,],[1,5,]),'function':([0,2,],[2,2,]),'empty':([0,2,7,8,15,16,20,50,61,64,65,72,],[3,3,10,13,13,21,21,62,69,21,21,69,]),'params':([7,],[9,]),'plist':([8,15,],[11,17,]),'statements':([16,20,64,65,],[19,31,70,71,]),'statement':([16,20,64,65,],[20,20,20,20,]),'attrib':([16,20,64,65,],[22,22,22,22,]),'if':([16,20,64,65,],[23,23,23,23,]),'while':([16,20,64,65,],[24,24,24,24,]),'return':([16,20,64,65,],[25,25,25,25,]),'logic':([28,29,32,33,45,50,68,],[34,41,42,43,55,61,72,]),'expression':([28,29,32,33,40,45,46,47,50,68,],[35,35,35,35,51,35,56,57,35,35,]),'term':([28,29,32,33,40,45,46,47,48,49,50,68,],[36,36,36,36,36,36,36,36,58,59,36,36,]),'call':([28,29,32,33,40,45,46,47,48,49,50,68,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'pcall':([50,],[60,]),'pclist':([61,72,],[67,75,]),}

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
  ('function -> FUNC ID LPAREN params RPAREN LBR statements RBR','function',8,'p_function','parser.py',42),
  ('pcall -> logic pclist','pcall',2,'p_params_call','parser.py',48),
  ('pcall -> empty','pcall',1,'p_params_call','parser.py',49),
  ('pclist -> COMMA logic pclist','pclist',3,'p_pclist','parser.py',58),
  ('pclist -> empty','pclist',1,'p_pclist','parser.py',59),
  ('params -> ID plist','params',2,'p_params','parser.py',67),
  ('params -> empty','params',1,'p_params','parser.py',68),
  ('plist -> COMMA ID plist','plist',3,'p_plist','parser.py',80),
  ('plist -> empty','plist',1,'p_plist','parser.py',81),
  ('statements -> statement statements','statements',2,'p_s','parser.py',89),
  ('statements -> empty','statements',1,'p_s','parser.py',90),
  ('statement -> attrib','statement',1,'p_statement','parser.py',97),
  ('statement -> if','statement',1,'p_statement','parser.py',98),
  ('statement -> while','statement',1,'p_statement','parser.py',99),
  ('statement -> return','statement',1,'p_statement','parser.py',100),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',105),
  ('if -> IF LPAREN logic RPAREN LBR statements RBR','if',7,'p_if','parser.py',109),
  ('while -> WHILE LPAREN logic RPAREN LBR statements RBR','while',7,'p_while','parser.py',118),
  ('return -> RETURN logic SEMICOLON','return',3,'p_return','parser.py',130),
  ('attrib -> ID ATTRIB logic SEMICOLON','attrib',4,'p_attrib','parser.py',134),
  ('logic -> logic LT logic','logic',3,'p_logic','parser.py',144),
  ('logic -> expression','logic',1,'p_logic_expression','parser.py',148),
  ('expression -> expression PLUS expression','expression',3,'p_e','parser.py',152),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parser.py',156),
  ('expression -> term','expression',1,'p_expression_term','parser.py',161),
  ('term -> term TIMES term','term',3,'p_term','parser.py',165),
  ('term -> term DIVIDE term','term',3,'p_term_div','parser.py',171),
  ('term -> call','term',1,'p_term_call','parser.py',176),
  ('term -> NUMBER','term',1,'p_term_number','parser.py',180),
  ('term -> ID','term',1,'p_term_id','parser.py',184),
  ('call -> ID LPAREN pcall RPAREN','call',4,'p_call','parser.py',194),
  ('term -> LPAREN expression RPAREN','term',3,'p_paren','parser.py',198),
]
