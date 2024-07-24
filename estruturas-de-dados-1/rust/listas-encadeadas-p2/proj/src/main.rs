#![allow(dead_code)]
#![allow(unused_variables)]


struct NoLista {
    info: i32,
    prox: Option<Box<NoLista>>
}

impl NoLista {
    fn new(info: i32) -> NoLista {
        NoLista { info, prox: None }
    }

    fn set_info(&mut self, info: i32) {
        self.info = info
    }

    fn get_info(&self) -> i32 {
        return self.info
    }

    fn set_prox(&mut self, prox: Option<Box<NoLista>>) {
        self.prox = prox
    }

    fn get_prox(&self) -> &Option<Box<NoLista>> {
        return &self.prox
    }

    fn to_string(&self) -> String {
        return self.info.to_string()
    }
}

struct Lista {
    prim: Option<Box<NoLista>>
}

impl Lista {
    fn new() -> Lista {
        Lista { prim: None }
    }

    fn insere(&mut self, v: i32) {
        let mut novo_no = Box::new(NoLista::new(v));
        novo_no.prox = self.prim.take();
        self.prim = Some(novo_no);
    }

    fn imprime(&self) {
        let mut atual = &self.prim;
        while let Some(no) = atual {
            print!("{} ", no.info);
            atual = &no.prox
        }
        print!("\n")
    }

    fn to_string(&self) -> String {
        let mut result = String::from("");
        let mut atual = &self.prim;
        while let Some(no) = atual {
            result += &no.info.to_string();
            result += &" ".to_string();
            atual = &no.prox
        }
        return result
    }

    fn vazia(&self) -> bool {
        return self.prim.is_none()
    }

    fn busca(&mut self, v: i32) -> Option<&mut NoLista> {
        let mut atual = &mut self.prim;
        while let Some(no) = atual {
            if no.info == v {
                return Some(&mut **no)
            }
            atual = &mut no.prox
        }
        return None
    }

    fn comprimento(&self) -> usize {
        let mut result: usize = 0;
        let mut atual = &self.prim;
        while let Some(no) = atual {
            result += 1;
            atual = &no.prox
        }
        return result
    }

    fn ultimo(&mut self) -> Option<&mut NoLista> {
        let mut atual = &mut self.prim;
        while let Some(no) = atual {
            if no.prox.is_none() {
                return Some(&mut **no);
            }
            atual = &mut no.prox;
        }
        return None;
    }

    fn retira(&mut self, v: i32) {
        let mut atual = &mut self.prim;
        let mut ant: Option<&mut NoLista> = None;
    
        while let Some(no) = atual {
            if no.info == v {
                match ant {
                    Some(node) => node.prox = no.prox.take(),
                    None => self.prim = no.prox.take(),
                }
                return;
            }
            ant = Some(no);
            atual = &mut no.prox;
        }
    }
    
    fn libera(&mut self) {
        let mut atual = self.prim.take();
        while let Some(mut no) = atual {
            atual = no.prox.take();
        }
    }
    
    fn insereFim(&mut self, v: i32) {
        let mut novo_no = Box::new(NoLista::new(v));
        match self.ultimo() {
            Some(ultimo_no) => {
                ultimo_no.prox = Some(novo_no);
            },
            None => {
                self.prim = Some(novo_no);
            }
        }
    }
    
    fn igual(&self, l: &Lista) -> bool {
        let mut atual1 = &self.prim;
        let mut atual2 = &l.prim;
        while let (Some(no1), Some(no2)) = (atual1, atual2) {
            if no1.info != no2.info {
                return false;
            }
            atual1 = &no1.prox;
            atual2 = &no2.prox;
        }
        return atual1.is_none() && atual2.is_none();
    }
}

fn main() {
    let mut lista = Lista::new();
    lista.insere(10);
    lista.insere(5);
    lista.insere(20);
    lista.insere(15);
    lista.insere(2);

    // println!("Lista:");
    // lista.imprime();
    // println!("");

    // lista.ultimo().unwrap().info = 50;

    // println!("Lista depois de ter seu último valor alterado:");
    // lista.imprime();
    // println!("");

    // println!("Comprimento da lista:");
    // println!("{}", lista.comprimento());
    // println!("");

    // println!("A lista está vazia?");
    // println!("{}", lista.vazia());
    // println!("");

    // println!("A lista está vazia?");
    // println!("{}", lista.vazia());
    // println!("");

    // println!("Buscando o nó com valor '20' e alterando seu dado para '-10':");
    // lista.busca(20).unwrap().info = -10;
    // lista.imprime();
    // println!("");

    // println!("Utilizando método 'to_string':");
    // println!("{}", lista.to_string());
}