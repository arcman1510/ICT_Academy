package com.spring.ecommerce.repository;
import com.spring.ecommerce.entity.Prodotto;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProdottoRepository extends JpaRepository<Prodotto, Long> {}