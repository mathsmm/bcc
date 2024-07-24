#[allow(unused)]

struct NoLista {
    v: i32,
    prox: Option<Box<NoLista>>
}

impl NoLista {
    fn new(v: i32) -> NoLista {
        NoLista { v: v, prox: None }
    }
}

struct Lista {
    head: Option<Box<NoLista>>,
    tail: Option<Box<NoLista>>
}

impl Lista {
    fn new() -> Lista {
        Lista { head: Option::None, tail: Option::None }
    }

    fn push_back(v: i32) {
        let novo_no = Some(Box::new(NoLista::new(v)));
        
    }
}

fn main() {

    println!("A");
}
