import pegpy
 peg = pegpy.grammar('chibi.tpeg')
 parser = pegpy.generate(peg)

 class Expr(object):
     @classmethod
     def new(cls,v):
         if isinstance(v,Expr):
             return v
         return Val(v)

class Val(Expr):
    __slot__=['value']

    def__init__(self,value):
        self.value = Value

    def__repr__(self):
        return f'Val({self.value})'

    def eval(self,env:dict):
        return self.values        
