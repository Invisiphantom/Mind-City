

检查ptr指向的值是否与expected相等
- 如果相等, 将ptr的值更新为desired, 并返回true
- 如果不等, 返回false并将ptr的值放入expected中
```c
bool __atomic_compare_exchange_n(type *ptr, type *expected, type desired, bool weak, int success_memorder, int failure_memorder)
{
    if (*ptr == *expected)
    {
        *ptr = desired;
        return true;
    }
    else
    {
        *expected = *ptr;
        return false;
    }
}
```


将val的值赋给ptr, 并返回ptr原来的值
```c
type __atomic_exchange_n (type *ptr, type val, int memmodel)
{
    type old = *ptr;
    *ptr = val;
    return old;
}
```