import decimal
from decimal import Decimal

ctx = decimal.getcontext()
print(type(ctx))
print(ctx)
print(ctx.prec)
print(ctx.rounding)
ctx.prec = 7
#ctx.rounding = decimal.ROUND_DOWN
print(ctx)

local_ctx_manager = decimal.localcontext()
print(type(local_ctx_manager))

x = Decimal('1.25')
y = Decimal('1.35')

#get context returns current context
with local_ctx_manager as ctx:
    ctx.prec = 20
    ctx.rounding = decimal.ROUND_HALF_UP
    print(decimal.getcontext())
    print(round(x,1))
    print(round(y, 1))

print(round(x, 1))
print(round(y, 1))

