package com.spring.ecommerce.service;
import com.spring.ecommerce.dto.*;
import com.spring.ecommerce.entity.*;
import com.spring.ecommerce.repository.*;
import com.spring.ecommerce.exception.*;
import org.springframework.stereotype.Service;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class VenditoreService {
    private final VenditoreRepository venditoreRepo;
    private final ProdottoRepository prodottoRepo;

    public VenditoreService(VenditoreRepository venditoreRepo, ProdottoRepository prodottoRepo) {
        this.venditoreRepo = venditoreRepo;
        this.prodottoRepo = prodottoRepo;
    }

    public VenditoreDTO aggiungiVenditore(VenditoreDTO dto) {
        Venditore venditore = new Venditore(null, dto.getNome(), dto.getCognome(), dto.getUsername(), dto.getPassword(), dto.getVia(), dto.getCitta(), new ArrayList<>());
        venditoreRepo.save(venditore);
        return toDTO(venditore);
    }

    public VenditoreDTO getVenditore(Long id) {
        Venditore v = venditoreRepo.findById(id).orElseThrow(() -> new ResourceNotFoundException("Venditore non trovato"));
        return toDTO(v);
    }

    public VenditoreBaseDTO getVenditoreBase(Long id) {
        Venditore v = venditoreRepo.findById(id).orElseThrow(() -> new ResourceNotFoundException("Venditore non trovato"));
        return new VenditoreBaseDTO(v.getId(), v.getNome(), v.getCognome(), v.getUsername(), v.getVia(), v.getCitta());
    }

    public VenditoreDTO aggiornaPassword(Long id, String nuovaPassword) {
        Venditore v = venditoreRepo.findById(id).orElseThrow(() -> new ResourceNotFoundException("Venditore non trovato"));
        v.setPassword(nuovaPassword);
        venditoreRepo.save(v);
        return toDTO(v);
    }

    public ProdottoDTO aggiungiProdotto(Long idVenditore, ProdottoDTO dto) {
        Venditore v = venditoreRepo.findById(idVenditore).orElseThrow(() -> new ResourceNotFoundException("Venditore non trovato"));
        Prodotto p = new Prodotto(null, dto.getDescrizione(), dto.getQuantita(), dto.getPrezzo(), dto.getSconto(), dto.getCategoria(), v);
        prodottoRepo.save(p);
        return toDTO(p);
    }

    public ProdottoDTO aggiornaQuantitaProdotto(Long idProdotto, int nuovaQuantita) {
        Prodotto p = prodottoRepo.findById(idProdotto).orElseThrow(() -> new ResourceNotFoundException("Prodotto non trovato"));
        p.setQuantita(nuovaQuantita);
        prodottoRepo.save(p);
        return toDTO(p);
    }

    private VenditoreDTO toDTO(Venditore v) {
        List<ProdottoDTO> prodotti = v.getProdotti().stream().map(this::toDTO).collect(Collectors.toList());
        return new VenditoreDTO(v.getId(), v.getNome(), v.getCognome(), v.getUsername(), v.getPassword(), v.getVia(), v.getCitta(), prodotti);
    }

    private ProdottoDTO toDTO(Prodotto p) {
        return new ProdottoDTO(p.getId(), p.getDescrizione(), p.getQuantita(), p.getPrezzo(), p.getSconto(), p.getCategoria());
    }
}