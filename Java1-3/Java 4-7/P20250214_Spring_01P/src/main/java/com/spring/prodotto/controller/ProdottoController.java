package com.spring.prodotto.controller;
import org.springframework.web.bind.annotation.*;

import com.spring.prodotto.dto.ProdottoDTO;
import com.spring.prodotto.dto.ProdottoNoIdDTO;
import com.spring.prodotto.dto.ReportDTO;
import com.spring.prodotto.service.ProdottoService;
import java.util.*;

@RestController
@RequestMapping("/prodotti")

public class ProdottoController {
    private final ProdottoService prodottoService;
    
    public ProdottoController(ProdottoService prodottoService) {
        this.prodottoService = prodottoService;
    }
    
    @PostMapping("/carica")
    public void caricaProdotto(@RequestBody ProdottoDTO prodottoDTO) {
        prodottoService.aggiungiProdotto(prodottoDTO);
    }
    
    @GetMapping("/lista")
    public List<ProdottoNoIdDTO> visualizzaProdotti() {
        return prodottoService.ottieniTuttiProdotti();
    }
    
    @GetMapping("/{id}")
    public ProdottoDTO visualizzaProdotto(@PathVariable int id) {
        return prodottoService.ottieniProdottoPerId(id);
    }
    
    @GetMapping("/report")
    public ReportDTO visualizzaReport() {
        return prodottoService.generaReport();
    }
}
