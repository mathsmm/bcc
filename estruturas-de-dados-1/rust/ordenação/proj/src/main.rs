use rand::seq::SliceRandom;


fn troca(v: &mut [f64], a: usize, b: usize) {
    let tmp: f64 = v[a];
    v[a] = v[b];
    v[b] = tmp;
}

//Bubble_sort
fn bubble_sort(n: usize, v: &mut [f64]) { 
    let mut i: usize = 0;
    while i < n - 1 {
        let mut j: usize = 0;
        let mut trocou: bool = false;
        while j < n - (i + 1) {
            if v[j] > v[j + 1] {
                troca(v, j, j + 1);
                trocou = true;
            }
            j += 1;
        }
        i += 1;
        if !trocou {
            break;
        }
    }
}


fn rec_bubble_sort(n: usize, v: &mut [f64]) {
    if n == 1 {
        return; //Retorno --> ()
    }

    let mut i: usize = 0;
    while i < n - 1 {
        if v[i] > v[i + 1] {
            troca(v, i, i + 1);
        }
        i += 1;
    }

    return rec_bubble_sort(n - 1, v);
}

//Quick_sort
fn particiona(v: &mut [f64], mut a: usize, mut b: usize) -> usize {
    let x: f64 = v[a];
    let mut i: usize = a;
    while i <= b {
        if v[i] < x {
            troca(v, a, i);
            a += 1;
            i += 1;
        } else if v[i] > x {
            troca(v, i, b);
            b -= 1;
        } else {
            i += 1;
        }
    }
    troca(v, a, b);
    return a;
}

fn quick_sort(v: &mut [f64], a: usize, b: usize) {
    if a < b {
        let indice_pivo: usize = particiona(v, a, b);
        quick_sort(v, a, indice_pivo - 1);
        quick_sort(v, indice_pivo + 1, b);
    }
}

//Merge-sort
fn merge_sort(a: &mut [i32], p: usize, r: usize) {
    if p < r {
        let q = (p + r) / 2;
        merge_sort(a, p, q);
        merge_sort(a, q + 1, r);
        merge(a, p, q, r);
    }
}

fn merge(a: &mut [i32], p: usize, q: usize, r: usize) {
    let n1 = q - p + 1;
    let n2 = r - q;
    let mut l = vec![0; n1 + 1];
    let mut r = vec![0; n2 + 1];
    for i in 0..n1 {
        l[i] = a[p + i];
    }
    for j in 0..n2 {
        r[j] = a[q + j + 1];
    }
    l[n1] = std::i32::MAX;
    r[n2] = std::i32::MAX;
    let mut i = 0;
    let mut j = 0;
    for k in p..=r {
        if l[i] <= r[j] {
            a[k] = l[i];
            i += 1;
        } else {
            a[k] = r[j];
            j += 1;
        }
    }
}


fn is_sorted<T: PartialOrd>(v: &[T]) -> bool {
    v.windows(2).all(|w| w[0] <= w[1])
}

fn main() {
    let tamanhos = [10, 100, 1000, 10000];
    let mut rng = rand::thread_rng();

    for tamanho in tamanhos.iter() {
        let mut v: Vec<f64> = (1..=*tamanho as i32).map(|x| x as f64).collect();
        v.shuffle(&mut rng);

        // Teste do bubble_sort
        let mut v1 = v.clone();
        bubble_sort(*tamanho, &mut v1);
        assert!(is_sorted(&v1));

        // Teste do rec_bubble_sort
        let mut v2 = v.clone();
        rec_bubble_sort(*tamanho, &mut v2);
        assert!(is_sorted(&v2));

        // Teste do quick_sort
        let mut v3 = v.clone();
        quick_sort(&mut v3, 0, *tamanho - 1);
        assert!(is_sorted(&v3));

        // Teste do merge_sort
        let mut v4: Vec<i32> = v.iter().map(|x| *x as i32).collect();
        merge_sort(&mut v4, 0, *tamanho - 1);
        assert!(is_sorted(&v4.iter().map(|x| *x as f64).collect::<Vec<f64>>()));
    }
}