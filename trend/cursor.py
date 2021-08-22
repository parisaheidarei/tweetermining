class Cursor(object): 
    """Pagination helper class""" 
  
    def __init__(self, method, *args, **kargs): 
        if hasattr(method, 'pagination_mode'): 
            if method.pagination_mode == 'cursor': 
                self.iterator = CursorIterator(method, args, kargs) 
            elif method.pagination_mode == 'id': 
                self.iterator = IdIterator(method, args, kargs) 
            elif method.pagination_mode == 'page': 
                self.iterator = PageIterator(method, args, kargs) 
            else: 
                raise TweepError('Invalid pagination mode.') 
        else: 
            raise TweepError('This method does not perform pagination') 