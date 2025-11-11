package com.spring.studente.dao;

import com.spring.studente.entity.Studente;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DaoStudente extends JpaRepository<Studente, Integer> {
    // Puoi aggiungere query personalizzate qui, se necessario
}
